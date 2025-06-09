let isLogin = false;

function toggleForm() {
    const nameRow = document.getElementById('firstRow');
    const form = document.getElementById('userForm');
    const toggleText = document.getElementById('toggleText');
    const toggleLink = document.getElementById('toggleLink');
    const submitBtn = document.getElementById('submitBtn');

    if(isLogin) {
        nameRow.style.display = '';
        form.action= '/register';
        submitBtn.textContent='Register';
        toggleText.textContent='Already have an account?';
        toggleLink.textContent='Login';
        isLogin = false;
    }else{
        nameRow.style.display = 'none';
        form.action= '/login';
        submitBtn.textContent='Login';
        toggleText.textContent='Dont have an account?';
        toggleLink.textContent='Register';
        isLogin = true;
    }
}