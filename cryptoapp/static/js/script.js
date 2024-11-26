let timeout;
const idleTimeLimit = 10 * 60 * 1000; // 10 minutes

function resetIdleTimer(){
    clearTimeout(timeout);
    timeout = setTimeout(logoutUser, idleTimeLimit);
}

function logoutUser() {
    windows.location.href= '/logout';
}

document.addEventListener('mousemove', resetIdleTimer);
document.addEventListener('keypress', resetIdleTimer);
document.addEventListener('click', resetIdleTimer);
document.addEventListener('scroll', resetIdleTimer);


resetIdleTimer();