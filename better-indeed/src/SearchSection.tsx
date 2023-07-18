import { Box, Typography, Button } from '@mui/material'
import React, { useState } from 'react'
import SearchBar from './SearchBar';
import { fetchJobs } from './routes/route';

function SearchSection() {
    const [jobs, setJobs] = useState([]);
    const [jobSearchData, setJobSearchData] = useState({ job_title: '', location: [], });

    const handleSearchJobs = async () => {
        const fetchedJobs = await fetchJobs(jobSearchData);
        setJobs(fetchedJobs);
    }

    return (
        <Box sx={{ height: '80vh', display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
            <SearchBar jobSearchData={jobSearchData} setJobSearchData={setJobSearchData} />
            <Button variant="contained" onClick={handleSearchJobs}>Search Jobs</Button>
            <Typography variant={'h1'}>Sent Data: {JSON.stringify(jobSearchData)}</Typography>
            <Typography variant={'h1'}>Jobs: {JSON.stringify(jobs)}</Typography>
        </Box>
    )
}

export default SearchSection
