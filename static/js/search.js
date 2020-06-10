function searchDelete() {
    document.querySelector('.footer-search-input_input').value = ''
    document.querySelector('.footer-search-delete').style.display = 'none'
    document.querySelector('.footer-search-delete-background').style.display = 'none'
    document.querySelector('.footer-search-input_input').style.width = '130%'
}
function showDeleteButton() {
    if ( document.querySelector('.footer-search-input_input').value != '' ) {
        document.querySelector('.footer-search-delete').style.display = 'block'
        document.querySelector('.footer-search-delete-background').style.display = 'block'
        document.querySelector('.footer-search-input_input').style.width = '120%'
    }
    else {
        document.querySelector('.footer-search-delete').style.display = 'none'
        document.querySelector('.footer-search-delete-background').style.display = 'none'
        document.querySelector('.footer-search-input_input').style.width = '130%'
    }
}
function searchDeleteDialogs() {
    document.querySelector('.dialog-search-input_input').value = ''
    document.querySelector('.dialog-search-delete').style.display = 'none'
    document.querySelector('.dialog-search-input_input').style.width = '100%'
}
function showDeleteButtonDialogs() {
    if ( document.querySelector('.dialog-search-input_input').value != '' ) {
        document.querySelector('.dialog-search-delete').style.display = 'block'
        document.querySelector('.dialog-search-input_input').style.width = '95%'
    }
    else {
        document.querySelector('.dialog-search-delete').style.display = 'none'
        document.querySelector('.dialog-search-input_input').style.width = '100%'
    }
}
document.getElementById('dialog-search-id').onfocus = function() {
    document.querySelector('.dialog-search-icon').style.color = "#ffffff";
}
document.getElementById('dialog-search-id').onblur = function() {
    document.querySelector('.dialog-search-icon').style.color = "#cccccc";
}
document.getElementById('footer-search-id').onfocus = function() {
    document.querySelector('.footer-search-icon').style.color = "#ffffff";
}
document.getElementById('footer-search-id').onblur = function() {
    document.querySelector('.footer-search-icon').style.color = "#cccccc";
}
