import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [filteredVar, setVar] = useState(0);

  useEffect(() => {
    fetch('/filter').then(res => res.json()).then(data => {
      setCurrentTime(data.testvar);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The variable returned from Python is {filteredVar}.</p>
      </header>
    </div>
  );
}

export default App;