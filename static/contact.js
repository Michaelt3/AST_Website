document.getElementById('nav-button').addEventListener('click', 
function() {
  document.querySelector('.contact-modal').style.display = 'flex';
});
document.querySelector('.close').addEventListener('click',
function() {
document.querySelector('.contact-modal').style.display = 'none';
});