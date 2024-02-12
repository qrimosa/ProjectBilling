// const openPopUp = $('#open_pop_up')
// const closePopUp = $('#close_pop_up');
// const loginClosePopUp = $('#close_pop_up_login');
// const popUp = $('#pop_up');
// const registerPopUp = $('#pop_up_body');
// const loginPopUp = $('#pop_up_body_login');


// openPopUp.addEventListener('click', (e) => {
//     e.preventDefault();
//     popUp.classList.add('active');
//     loginPopUp.classList.remove('pop_up_body_login')
//     registerPopUp.classList.add('pop_up_register')
// })

// closePopUp.addEventListener('click', () => {
//     popUp.classList.remove('active');
// })
// loginClosePopUp.addEventListener('click', () => {
//     popUp.classList.remove('active');
// })

// function registerClick() {
//     loginPopUp.classList.remove('pop_up_body_login')
//     registerPopUp.classList.add('pop_up_register')
// }
// function loginClick() {
//     registerPopUp.classList.remove('pop_up_register')
//     loginPopUp.classList.add('pop_up_body_login')
// }
$(document).ready(() => {
    $("#open_pop_up").click((e) => {
        e.preventDefault();
        $('#pop_up').addClass('active');
        $('#pop_up_body_login').removeClass('pop_up_body_login');
        $('#pop_up_body').addClass('pop_up_register');
    })
    $('.pop_up_close').click(() => {
        $('#pop_up').removeClass('active');
    })
    $('.registerClick').click(() => {
        $('#pop_up_body_login').removeClass('pop_up_body_login');
        $('#pop_up_body').addClass('pop_up_register');
    })
    $('.loginClick').click(() => {
        $('#pop_up_body').removeClass('pop_up_register');
        $('#pop_up_body_login').addClass('pop_up_body_login');
    })
    $('.button').click(() => {
        $.ajax({
            url: 'reg/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                email: $('input[name=email]').val(),
                login: $('input[name=login]').val(),
                password: $('input[name=password]').val(),
            }
        })

    })
    $('.button2').click(() => {
        $.ajax({
            url: 'auth/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                username: $('input[name=username]').val(),
                password: $('input[name=loginPassword]').val(),
            },
            success: function () {
                window.location.assign("auth")
            }
        })
    })
})