const fs = require('fs');
function readDimensions(path) {
    const buffer = fs.readFileSync(path);
    // Assuming PNG
    const width = buffer.readUInt32BE(16);
    const height = buffer.readUInt32BE(20);
    return `${width}x${height}`;
}
console.log('DIVE:', readDimensions('nahyun_imported/image_source/Projects_Products/thumnail_DIVE.png'));
console.log('News:', readDimensions('nahyun_imported/image_source/Projects_Products/thumnail_news.png'));
console.log('Hopzie:', readDimensions('nahyun_imported/image_source/Projects_Products/thumnail_hopzie.png'));
console.log('Just do it:', readDimensions('nahyun_imported/image_source/Projects_Products/thumnail_just do it.png'));
