
document.addEventListener('DOMContentLoaded', function() {
 
  const form = document.querySelector('form');
  if (form) {
    form.addEventListener('submit', function(event) {
      const titulo = document.getElementById('titulo');
      const detalhes = document.getElementById('detalhes');
      
      if (titulo && titulo.value.trim() === '') {
        alert('Por favor, preencha o título da nota.');
        event.preventDefault();
        titulo.focus();
        return false;
      }
      
      if (detalhes && detalhes.value.trim() === '') {
        alert('Por favor, preencha os detalhes da nota.');
        event.preventDefault();
        detalhes.focus();
        return false;
      }
    });
  }
  const inputs = document.querySelectorAll('input[type="text"], textarea');
  inputs.forEach(input => {
    input.addEventListener('focus', function() {
      this.style.borderColor = '#f7d736';
    });
    
    input.addEventListener('blur', function() {
      this.style.borderColor = '#ddd';
    });
  });
});
