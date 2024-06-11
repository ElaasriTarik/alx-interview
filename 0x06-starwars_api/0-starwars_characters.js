#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, async function (error, response, body) {
  if (error) return (error);

  const characters = JSON.parse(body).characters;
  for (const key in characters) {
    const result = await new Promise((resolve, reject) => {
      request(characters[key], function (error, response, body) {
        if (error) return (error);
        resolve(JSON.parse(body).name);
      });
    }
    );
    console.log(result);
  }
  // printCharacters(res.characters);
});

// async function printCharacters (characters) {
//   for (const character of characters) {
//     if (character === undefined) { return; }
//     const url = character;
//     await fetch(url)
//       .then(response => response.json())
//       .then(data => console.log(data.name));
//   }
// }
