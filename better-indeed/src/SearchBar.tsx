import React from 'react';
import { Stack, Autocomplete, TextField, Typography, Paper, Box } from "@mui/material";

export default function SearchBar({ jobSearchData, setJobSearchData }: any) {

    const states = [
        'AA',
        'AB',
        'AE',
        'EE',
    ];

    return (
        <Box
            sx={{
                display: 'flex',
                flexWrap: 'wrap',
                '& > :not(style)': {
                    m: 1,
                    width: 1000,
                    height: 250,
                },
                alignItems: 'center', justifyContent: 'center'
            }}
        >

            <Paper elevation={3} sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'space-evenly' }}>
                <Typography color="black" variant='h4' sx={{ mb: 1 }}>Let's get you hired</Typography>
                <Stack spacing={4} direction="row" sx={{ alignItems: 'center', justifyContent: 'center' }}>
                    <TextField id="outlined-basic" label="Job Title" variant="outlined" value={jobSearchData.job_title} onChange={(e) => setJobSearchData({ ...jobSearchData, job_title: e.target.value })} />
                    <Autocomplete
                        multiple
                        disablePortal
                        id="state-box"
                        options={states}
                        getOptionLabel={(option) => option}
                        sx={{ width: 300 }}
                        value={jobSearchData.location}
                        onChange={(event, newValue) => {
                            setJobSearchData({ ...jobSearchData, location: newValue || [] });
                        }}
                        renderInput={(params) => <TextField {...params} label="Location" variant="outlined" />}
                    />
                </Stack>
            </Paper>
        </Box>
    );
}
