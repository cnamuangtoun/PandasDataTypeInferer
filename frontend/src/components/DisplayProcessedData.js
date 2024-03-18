import React from 'react';


function DisplayProcessedData({ data }) {
    console.log(typeof data)
    const columnNames = data.length > 0 ? Object.keys(data[0]) : [];

    return (
        <div>
        <table>
            <thead>
            <tr>
                {columnNames.map((columnName, index) => (
                <th key={index}>{columnName}</th>
                ))}
            </tr>
            </thead>
            <tbody>
            {data.map((row, rowIndex) => (
                <tr key={rowIndex}>
                {columnNames.map((columnName, colIndex) => (
                    <td key={colIndex}>{row[columnName] !== null ? row[columnName] : 'N/A'}</td>
                ))}
                </tr>
            ))}
            </tbody>
        </table>
        </div>
    );
}

export default DisplayProcessedData;
