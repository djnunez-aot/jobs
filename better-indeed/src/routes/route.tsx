export const fetchJobs = async ({ job_title, location }: any): Promise<any> => {

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ job_title, location })
    };

    return fetch('http://127.0.0.1:5000/api/scraper', requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json()
        })
        .then(data => data)
        .catch(err => console.error('Fetch Error: ', err)); // Log any fetch errors
}
