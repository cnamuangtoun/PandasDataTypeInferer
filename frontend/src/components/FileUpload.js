import React, { useState } from 'react';
import axios from 'axios';
import DisplayProcessedData from './DisplayProcessedData';



function FileUpload() {
  const [file, setFile] = useState(null);
  const [processedData, setProcessedData] = useState(null);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a file to upload.");
      return;
    }
    setError("");
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      const parsedData = JSON.parse(response.data.processed_data);
      const dataTypes = response.data.data_types;

      setProcessedData({ parsedData , dataTypes });
    } catch (error) {
      console.error('Error uploading file:', error);
      setError('Error uploading file', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" />
        <button type="submit">Upload</button>
      </form>
      {error && <div>{error}</div>}
      {processedData && (<DisplayProcessedData data={processedData.parsedData} dataTypes={processedData.dataTypes}/>)}
    </div>
  );
} 

export default FileUpload;