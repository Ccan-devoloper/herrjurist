import fs from 'node:fs';
import {randomBytes, createCipheriv, publicEncrypt, constants} from 'node:crypto';
import {THEMEN} from '../../daten/themen.mjs';

const matches = THEMEN.filter(entry => /willenserkl(?:ä|ae)r/i.test(JSON.stringify(entry)));
const key = randomBytes(32);
const iv = randomBytes(12);
const cipher = createCipheriv('aes-256-gcm', key, iv);
const plaintext = Buffer.from(JSON.stringify(matches));
const ciphertext = Buffer.concat([cipher.update(plaintext), cipher.final()]);
const wrappedKey = publicEncrypt({key: "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAztQMJCDpAc/GBF/NYkwb\nmknDk8mhkz+QCYJIR7eRhX6uTzXsg6wRpK8t0WQdeSGgqByfzCZeebR+JCP4ZdZU\naspb8rsqIA5T54KuCWprADT9kR+VUp2Rgd0vgxH7ZsmE5ePn/Dckoanig/AOgqB5\nKiJhhYsoz4XNrpxv5I2MxIUkmBvlZnRkdDPJXkNFp/az2eKnm+U8X0g42nj/DiTY\nBlJNzhqokZ1mJPDPMt1emgDT3ynb/Q6CPIHiyP2QPyNgNRTNnyqrPQWSfmzaD6cq\n9v5VL1EiqYVsesF9Wsbj4QnFpoqlYCGqcANxj5VR3RZ9IJf6VP+QyMaL/bQWFEs3\nEQIDAQAB\n-----END PUBLIC KEY-----\n", padding: constants.RSA_PKCS1_OAEP_PADDING, oaepHash: 'sha256'}, key);
fs.mkdirSync('youtube/willenserklaerung/work', {recursive:true});
fs.writeFileSync('youtube/willenserklaerung/work/topic.enc.json', JSON.stringify({
  algorithm:'AES-256-GCM/RSA-OAEP-SHA256',
  wrappedKey:wrappedKey.toString('base64'),
  iv:iv.toString('base64'),
  tag:cipher.getAuthTag().toString('base64'),
  ciphertext:ciphertext.toString('base64')
}));
console.log('Willenserklärung matches:', matches.length);
