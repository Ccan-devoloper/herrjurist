import fs from 'node:fs';
import { generateKeyPairSync, randomBytes, publicEncrypt, createCipheriv, webcrypto } from 'node:crypto';

// Public key can be committed. Keep the private key outside the repository.
const [mode, ...args] = process.argv.slice(2);
if (mode === '--generate-key') {
  const [privatePath, publicPath] = args;
  if (!privatePath || !publicPath || fs.existsSync(privatePath) || fs.existsSync(publicPath)) throw new Error('Key paths missing or already exist');
  const { privateKey, publicKey } = generateKeyPairSync('rsa', {
    modulusLength: 3072,
    publicExponent: 0x10001,
    publicKeyEncoding: { type: 'spki', format: 'pem' },
    privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
  });
  fs.writeFileSync(privatePath, privateKey, { mode: 0o600, flag: 'wx' });
  fs.writeFileSync(publicPath, publicKey, { mode: 0o644, flag: 'wx' });
  console.log('Key pair generated; private key must remain outside GitHub.');
} else if (mode === '--encrypt') {
  const [publicPath, htmlPath, metadataPath, outputPath] = args;
  const payload = { ...JSON.parse(fs.readFileSync(metadataPath, 'utf8')), html: fs.readFileSync(htmlPath, 'utf8') };
  if (!payload.kit_id || !payload.subject || !payload.html) throw new Error('Incomplete preview payload');
  const key = randomBytes(32);
  const iv = randomBytes(12);
  const cipher = createCipheriv('aes-256-gcm', key, iv);
  const ciphertext = Buffer.concat([cipher.update(JSON.stringify(payload), 'utf8'), cipher.final(), cipher.getAuthTag()]);
  const wrappedKey = publicEncrypt({ key: fs.readFileSync(publicPath), oaepHash: 'sha256' }, key);
  fs.writeFileSync(outputPath, JSON.stringify({ version: 1, algorithm: 'RSA-OAEP-256+A256GCM', key: wrappedKey.toString('base64'), iv: iv.toString('base64'), ciphertext: ciphertext.toString('base64') }) + '\n');
  console.log(`Encrypted preview: ${ciphertext.length} ciphertext bytes`);
} else if (mode === '--verify') {
  const [privatePath, envelopePath] = args;
  const pem = fs.readFileSync(privatePath, 'utf8');
  const der = Buffer.from(pem.replace(/-----[^-]+-----|\s/g, ''), 'base64');
  const key = await webcrypto.subtle.importKey('pkcs8', der, { name: 'RSA-OAEP', hash: 'SHA-256' }, false, ['decrypt']);
  const envelope = JSON.parse(fs.readFileSync(envelopePath, 'utf8'));
  const rawKey = await webcrypto.subtle.decrypt({ name: 'RSA-OAEP' }, key, Buffer.from(envelope.key, 'base64'));
  const aes = await webcrypto.subtle.importKey('raw', rawKey, 'AES-GCM', false, ['decrypt']);
  const clear = await webcrypto.subtle.decrypt({ name: 'AES-GCM', iv: Buffer.from(envelope.iv, 'base64') }, aes, Buffer.from(envelope.ciphertext, 'base64'));
  const payload = JSON.parse(new TextDecoder().decode(clear));
  if (!payload.html.includes('LÖSUNGSSKIZZE')) throw new Error('Preview integrity check failed');
  console.log(JSON.stringify({ kit_id: payload.kit_id, subject: payload.subject, htmlLength: payload.html.length }));
} else throw new Error('Usage: --generate-key <private.pem> <public.pem> | --encrypt <public.pem> <html> <metadata.json> <output.enc.json> | --verify <private.pem> <output.enc.json>');
