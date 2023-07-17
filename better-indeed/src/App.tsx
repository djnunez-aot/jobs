import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';
import SearchSection from './SearchSection';
import { fetchJobs } from './routes/route';
import { Button, Typography } from '@mui/material';


function App() {

  return (
    <div className="App App-header">
      <Navbar />
      <SearchSection />
    </div>
  );
}

export default App;
