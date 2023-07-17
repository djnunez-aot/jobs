import { Box, Typography, Button } from '@mui/material'
import React, { useState } from 'react'
import SearchBar from './SearchBar';
import { fetchJobs } from './routes/route';

function SearchSection() {
    const [jobs, setJobs] = useState([]);
    const [jobSearchData, setJobSearchData] = useState({ title: '', location: [], });

    return (
        <Box sx={{ height: '80vh', display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
            <SearchBar jobSearchData={jobSearchData} setJobSearchData={setJobSearchData} />
            <Button variant="contained" onClick={() => fetchJobs}>Search Jobs</Button>
            <Typography variant={'h1'}>{JSON.stringify(jobSearchData)}</Typography>
        </Box>
    )
}

export default SearchSection