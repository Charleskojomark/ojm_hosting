document.addEventListener('DOMContentLoaded', () => {
    // Show only the selected section
    window.showSection = function(sectionId) {
        document.getElementById('subscribe-section').style.display = 'none';
        document.getElementById('fund-wallet-section').style.display = 'none';
        document.getElementById(sectionId).style.display = 'block';
    };

    // Set the amount value
    window.setAmount = function(amount, inputId) {
        document.getElementById(inputId).value = amount;
    };
});
