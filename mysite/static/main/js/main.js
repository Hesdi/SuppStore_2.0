let close_alert =document.querySelector('.close-alert')
let alert_div = document.querySelector('.alert')

close_alert.addEventListener('click', ()=>{
  alert_div.style.display = 'none'
})