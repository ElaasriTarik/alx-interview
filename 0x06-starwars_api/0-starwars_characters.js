#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, async function (error, response, body) {
  if (error) return (error);

  const res = JSON.parse(body);
  printCharacters(res.characters);
});

function printCharacters (characters) {
  for (const character in characters) {
    const url = 'https://swapi-api.hbtn.io/api/people/' + character;
    request(url, async function (error, response, body) {
      if (error) return (error);

      const res = JSON.parse(body);
      console.log(res.name);
    });
  }
}
