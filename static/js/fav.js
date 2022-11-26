$(document).ready(function() {

    $('.to-fav').on('click', function(e) {
        e.preventDefault();
        let pk_photo = e.target.id;

        url = `http://127.0.0.1:8000/api/photo/${ pk_photo }/tofav/`

    fetch(url)
    .then((response) => {

        document.getElementById(pk_photo).innerText = 'Удалить из избранного'
        $(this).removeClass('to-fav').addClass('from-fav');
        $(this).innertext = 'jjj';
        return response;
        })
    });

    $('.from-fav').on('click', function(e) {
        e.preventDefault();
        let pk_photo = e.target.id;
        url = `http://127.0.0.1:8000/api/photo/${ pk_photo }/fromfav/`

    fetch(url)
    .then((response) => {

        document.getElementById(pk_photo).innerText = 'Добавить в избранное'
        $(this).removeClass('from-fav').addClass('to-fav')

        return response;
        })
    })

    })
