
// JavaScript for handling profile modal and other interactions
document.getElementById('userImage').addEventListener('click', function () {
    document.getElementById('profileModal').style.display = 'flex';
});

document.getElementById('closeModal').addEventListener('click', function () {
    document.getElementById('profileModal').style.display = 'none';
});

document.getElementById('changeImage').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('modalUserImage').src = e.target.result;
            document.getElementById('userImage').src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});
