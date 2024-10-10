document.querySelectorAll('.increase').forEach(function(button) {
    button.addEventListener('click', function() {
        let counterInput = this.parentElement.querySelector('.counterInput');
        counterInput.value = parseInt(counterInput.value) + 1;
    });
});

document.querySelectorAll('.decrease').forEach(function(button) {
    button.addEventListener('click', function() {
        let counterInput = this.parentElement.querySelector('.counterInput');
        if (parseInt(counterInput.value) > 0) {
            counterInput.value = parseInt(counterInput.value) - 1;
        } else {
            counterInput.value = 0;
        }
    });
});

// Prevent users from entering negative numbers manually
document.querySelectorAll('.counterInput').forEach(function(input) {
    input.addEventListener('input', function() {
        if (this.value < 0) {
            this.value = 0;
        }
    });
});