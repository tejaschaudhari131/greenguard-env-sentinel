# GreenGuard: An Environmental Sentinel

GreenGuard is a cutting-edge platform designed to monitor and mitigate environmental pollution using satellite imagery and machine learning. The platform provides real-time tracking of pollution levels in rivers, lakes, and land areas, empowering stakeholders to take timely action. The web-based platform offers interactive maps, real-time alerts, and tools for collaborative analysis.

## Features

### Pollution Detection:
- Leverages satellite imagery to detect pollution in water bodies (rivers, lakes) and land areas.
- Machine learning algorithms identify pollution sources and assess severity levels.
- Works with both historical and real-time data from satellite feeds.

### Real-time Monitoring:
- Interactive web interface for visualizing pollution data on a geographical map.
- Real-time alerts for stakeholders when pollution levels exceed predefined thresholds.
- Integration with Google Maps for detailed geographical context.

### Collaboration Tools:
- Multi-user collaboration support to allow team-based analysis.
- Ability to share pollution insights and reports with other users.
- Easy-to-use data export options for generating pollution analysis reports.

## Technology Stack

- **Backend**: Python (Flask), TensorFlow (for machine learning models).
- **Frontend**: JavaScript, HTML, CSS (for user interaction and visualization).
- **APIs**: Google Maps API, Google Earth Engine (for satellite data and geographical context).
- **Cloud**: Google Cloud Platform (GCP) for deployment, scalability, and data storage.

## Installation

### Prerequisites:
- **Python**: Ensure you have Python 3.7+ installed.
- **API Keys**: You need API keys for:
  - Google Maps API
  - Google Earth Engine (GEE)
  
### Steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tejaschaudhari131/greenguard-env-sentinel.git
   cd greenguard-env-sentinel
   ```

2. **Install Dependencies**:
   Use the following command to install all required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   - Rename the `.env.example` file to `.env`:
     ```bash
     mv .env.example .env
     ```
   - Add your Google Maps and Google Earth Engine API keys to the `.env` file:
     ```bash
     GOOGLE_MAPS_API_KEY=your_google_maps_api_key
     GOOGLE_EARTH_ENGINE_CREDENTIALS=your_earth_engine_api_key
     ```

4. **Run the Application**:
   Start the Flask application locally:
   ```bash
   python app.py
   ```
   The application will run on `http://localhost:5000`.

## Usage

1. **Monitor Pollution**: 
   - Once the application is running, visit `http://localhost:5000` in your browser.
   - Use the interactive map to view real-time pollution data.
   - Upload satellite images for pollution detection using built-in tools.

2. **Analyze Trends**:
   - Use the analysis tools to observe trends in pollution over time.
   - Generate pollution reports from the platform to share with other stakeholders.

3. **Collaborate**:
   - Invite other users to collaborate on pollution data analysis.
   - Use the built-in tools to share findings, comments, and insights with your team.

## Machine Learning Model

The pollution detection model is powered by TensorFlow. The pre-trained model is used to analyze satellite images and identify pollution in specific regions.

- **Model Training**: You can retrain the model using custom data by modifying the `train_model.py` script.
- **Model Path**: The default model is stored in the `models/pollution_model.h5` file.

## Deployment

To deploy GreenGuard on a cloud platform (e.g., Google Cloud), follow these steps:

1. **Google Cloud Setup**:
   - Create a project on Google Cloud Platform (GCP).
   - Enable the required APIs (Google Maps, Google Earth Engine).
   - Set up Google Cloud App Engine or Google Compute Engine for deployment.

2. **Deploy**:
   - Use the following command to deploy to Google App Engine:
     ```bash
     gcloud app deploy
     ```
   - For Compute Engine, follow the setup for virtual machines and containerized deployments.

## Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the Repository**: 
   - Click the "Fork" button on the top right of this page to create a copy of the repository.
   
2. **Create a New Branch**:
   - Create a branch for your new feature or bug fix:
     ```bash
     git checkout -b feature/new-feature
     ```

3. **Make Your Changes**:
   - Write your code, test it thoroughly, and ensure it follows the style guidelines.

4. **Submit a Pull Request**:
   - Open a pull request from your branch to the main branch of the repository.
   - Please provide a detailed description of your changes in the PR description.

## License

This project is licensed under the MIT License. You can see the full license in the [LICENSE](./LICENSE) file.

## Contact

If you have any inquiries or need support, please feel free to contact:

- **Tejaram Chaudhari**: [tejaschaudhari131@gmail.com](mailto:tejaschaudhari131@gmail.com)

---

## Acknowledgments

- **Google Earth Engine**: For providing satellite data and APIs.
- **Google Maps API**: For providing the geographical data and visualization tools.

## Resources

- [Google Maps API Documentation](https://developers.google.com/maps/documentation)
- [Google Earth Engine Documentation](https://developers.google.com/earth-engine/)

---

## Project Activity

- Stars: 0 stars
- Forks: 0 forks
- Watchers: 1 watcher

Stay tuned for upcoming releases, and feel free to contribute to the project!

---

© 2024 GreenGuard, Inc.

--- 

**Note**: Make sure that you have all dependencies installed and the required API keys to access Google services. Keep your API keys secure and do not share them publicly.

