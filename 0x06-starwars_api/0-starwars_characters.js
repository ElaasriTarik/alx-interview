#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, async function (error, response, body) {
  if (error) return (error);

  const res = JSON.parse(body);
  printCharacters(res.characters);
});

function printCharacters (characters) {
  // console.log(characters)
  for (const character of characters) {
    if (character === undefined) { return; }
    const url = character;
    request(url, async function (error, response, body) {
      if (error) return (error);

      const res = JSON.parse(body);
      console.log(res.name);
    });
  }
}
