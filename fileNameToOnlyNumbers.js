const fs = require("fs");
const path = require("path");

const directoryPath = path.join(__dirname, "processed_output");

fs.readdir(directoryPath, (err, files) => {
  if (err) {
    return console.log("Unable to scan directory: " + err);
  }

  let index = 2033;

  files.forEach((file) => {
    const match = file.match(/\d+/g);
    const filePath = path.join(directoryPath, file);

    if (match) {
      const oldFilePath = path.join(directoryPath, file);
      const fileExtension = path.extname(file); // 파일 확장자 추출

      if (fileExtension === ".jpeg") {
        const newFilePath = path.join(
          directoryPath,
          `${index}${fileExtension}`
        );

        fs.renameSync(oldFilePath, newFilePath);
        index++; // 인덱스 증가
      }

      if (fileExtension === ".jpg") {
        const newFilePath = path.join(directoryPath, `${index}.jpeg`);

        fs.renameSync(oldFilePath, newFilePath);
        index++; // 인덱스 증가
      }

      // 파일 이름 변경
    }
  });
});
