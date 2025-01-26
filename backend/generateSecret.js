// backend/generateSecret.js
const crypto = require('crypto');

const generateSecret = () => {
    return crypto.randomBytes(64).toString('hex'); // Generates a 64-byte random string
};

console.log(generateSecret());