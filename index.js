const movieNameFieldElement = document.getElementById('movie-name-field');
const movieNameButtonElement = document.getElementById('movie-name-button');
const movieNameElement = document.getElementById('movie-name');
const movieRatingElement = document.getElementById('movie-rating');
const moviePlotElement = document.getElementById('movie-plot');


console.log('test')
movieNameButtonElement.onclick = (e) =>
{
    let movieName = movieNameFieldElement.value;

    console.log(movieName)
    fetch(`http://127.0.0.1:8000/api/movie/${movieName}`).then(response => {
        if (!response.ok)
        {
            throw new Error(`HTTP ERROR! Status: ${response.status}`);
        }

        return response.json();


        


    }).then(data =>
    {
        movieNameElement.textContent = data.name;
        movieRatingElement.textContent = data.rating;
        moviePlotElement.textContent = data.plot;
    }
    ).catch(error => {
        console.error("Error:", error);
    })


    e.preventDefault();
}


