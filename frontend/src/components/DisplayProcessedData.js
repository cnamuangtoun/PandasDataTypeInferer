import React from 'react';


function formatDate(timestamp) {
    if (!timestamp) return '';
    
    const date = new Date(timestamp);
    return date.toLocaleString(); // Formats to local date and time
}

function DisplayProcessedData({ data, dataTypes }) {

    const formatValue = (value, type) => {
        if (type === 'datetime64[ns]' && value) {
          return formatDate(value);
        }
        return value;
    };

    console.log(data);
    console.log(dataTypes);

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
                        <td key={colIndex}>
                        {row[columnName] !== null ? 
                            formatValue(row[columnName], dataTypes[columnName]) : 'N/A'}
                        </td>
                    ))}
                </tr>
            ))}
            </tbody>
        </table>
        </div>
    );
}

export default DisplayProcessedData;
