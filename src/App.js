import './App.css';
import React from 'react';

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            resources: []
        }

    }

    componentDidMount() {
        fetch("http://127.0.0.1:5001/api/resources")
            .then(res => {
                if (!res.ok) {
                    throw new Error("HTTP error " + res.status);
                }
                return res.json();
            })
            .then(data => {
                this.setState({ resources: data });
            })
            .catch(err => {
                console.error("Failed to fetch resources from backend:", err);
            });
    }

    render() {
        const { resources } = this.state;
        const imageUrl = process.env.REACT_APP_S3_IMAGE_URL ||
            (process.env.REACT_APP_S3_BUCKET_URL && process.env.REACT_APP_S3_IMAGE_KEY
                ? `${process.env.REACT_APP_S3_BUCKET_URL.replace(/\/+$/, '')}/${process.env.REACT_APP_S3_IMAGE_KEY.replace(/^\/+/, '')}`
                : null);

        return (
            <div className="App">
                <header className="App-header">
                    {imageUrl && (
                        <img
                            className="s3-banner"
                            src={imageUrl}
                            alt="S3 banner"
                            style={{ maxWidth: '90%', height: 'auto', marginBottom: '24px' }}
                        />
                    )}
                    <table className="trial-data">
                        <thead>
                            <tr><th>Room Number</th>
                                <th>Floor Number</th>
                                <th>Room Status</th></tr></thead>
                        <tbody>
                            {resources.map(resource => (
                                <tr key={resource.Name}><td>{resource.Name}</td>
                                    <td>{resource.Data.Value.FloorNumber}</td>
                                    <td>{resource.State}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </header>
            </div>
        );
    };
}

export default App;
