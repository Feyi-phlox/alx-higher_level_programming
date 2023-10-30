#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Function to fetch character data and print names
    function fetchCharacterData (index) {
      if (index < characterUrls.length) {
        request(characterUrls[index], (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else if (charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            console.error(`Failed to retrieve character data. Status code: ${charResponse.statusCode}`);
          }

          // Fetch data for the next character
          fetchCharacterData(index + 1);
        });
      }
    }

    // Start fetching character data from the first character
    fetchCharacterData(0);
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});
