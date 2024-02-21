const fs = require('fs')

// Get file path from command line argument
const filePath = process.argv[2]

// Read the content of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // If an error occurred during reading, print the error object
    console.error(err)
  } else {
    // If reading is successful, print the content of the file
    console.log(data)
  }
})

