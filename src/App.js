import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from "react";
import { Button, MenuItem, Select, TextField } from "@mui/material";

import { API } from 'aws-amplify';

function App() {
  const [inputString, setInputString] = useState();
  const [outputString, setOutputString] = useState();
  const [srcLanguage, setSrcLanguage] = useState();
  const [destLanguage, setDestLanguage] = useState();


  const handleTranslateClicked = () => {
    window.alert(inputString+' ,'+srcLanguage+' ,'+destLanguage);
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json", "charset=iso-8859-1");

    var raw = JSON.stringify({
      srcLanguage,
      destLanguage,
      inputString
    });

    var requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
    };

    fetch("https://svbmgct8kd.execute-api.us-east-1.amazonaws.com/dev/translate", requestOptions)
      .then((response) => response.text())
      .then((result) => setOutputString(result))
      .catch((error) => setOutputString("error: " + error));
  };

  return (
    <div className="App">
      <TextField
        id="input-string"
        label="Multiline"
        multiline
        rows={4}
        value={inputString}
        onChange={(e) => setInputString(e.target.value)}
      />
      <Select
        labelId="source-lang-label"
        id="source-lang"
        value={srcLanguage}
        label="Source Language"
        onChange={(e) => {
          console.log(e.target.value);
          setSrcLanguage(e.target.value);
        }}
      >
        <MenuItem value={"en"}>English</MenuItem>
        <MenuItem value={"de"}>German</MenuItem>
        <MenuItem value={"fr"}>French</MenuItem>
      </Select>

      <Select
        labelId="dest-lang-label"
        id="dest-lang"
        value={destLanguage}
        label="Destination Language"
        onChange={(e) => setDestLanguage(e.target.value)}
      >
        <MenuItem value={"en"}>English</MenuItem>
        <MenuItem value={"de"}>German</MenuItem>
        <MenuItem value={"fr"}>French</MenuItem>
      </Select>
      <Button variant="contained" onClick={handleTranslateClicked}>
        Translate
      </Button>
      <meta charset="utf-8" />
      <div>{outputString}</div>
    </div>
  );
}

export default App;
