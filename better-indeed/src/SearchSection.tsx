import { Box, Typography } from '@mui/material'
import React from 'react'
import SearchBar from './SearchBar'

function SearchSection() {
    return (
        <Box>
            <Typography variant='h1'>Let's get you hired?</Typography>
            <SearchBar />
        </Box>
    )
}

export default SearchSection