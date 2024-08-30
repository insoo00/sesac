$(document).ready(function(){
    const type = ['Back-end', 'Front-end', 'Full-stack'];
    let index = 0;
    let charIndex = 0;
    let currentText = '';

    function typeText() {
        if (charIndex < type[index].length) {
            currentText += type[index].charAt(charIndex);
            $('#developer-type').text(currentText);
            charIndex++;
            setTimeout(typeText, 100);
        } else {
            setTimeout(function() {
                index = (index + 1) % type.length;
                charIndex = 0;
                currentText = '';
                typeText();
            }, 1000);
        }
    }

    typeText();
});