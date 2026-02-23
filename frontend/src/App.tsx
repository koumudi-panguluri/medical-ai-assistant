import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import { PatientSelection } from './pages/PatientSelection';
import { AnalysisResults } from './pages/AnalysisResults';

function App() {
    return (
        <Router>
            <div className="app">
                <Routes>
                    <Route path="/" element={<PatientSelection />} />
                    <Route path="/analyze/:patientId" element={<AnalysisResults />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;