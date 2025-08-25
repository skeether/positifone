export default function handler(req, res) {
    fetch('https://ipapi.co/json/')
        .then(response => {
            if (!response.ok) throw new Error('API request failed');
            return response.json();
        })
        .then(data => res.status(200).json(data))
        .catch(error => {
            console.error('Error fetching visitor info:', error);
            res.status(500).json({
                ip: 'N/A',
                country_name: 'N/A',
                region: 'N/A',
                city: 'N/A',
                latitude: 'N/A',
                longitude: 'N/A',
                timezone: 'N/A',
                org: 'N/A',
                asn: 'N/A',
                postal: 'N/A',
                currency: 'N/A',
                languages: 'N/A'
            });
        });
}