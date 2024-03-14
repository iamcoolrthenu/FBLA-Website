function setJobTitle() {
    const params = new URLSearchParams(window.location.search);
    const jobTitle = params.get('job');
    document.getElementById('job-title').innerText = jobTitle || 'Job Title';
}