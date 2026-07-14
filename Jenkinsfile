pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt
                "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install pytest pytest-html
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                if not exist reports mkdir reports
                "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest tests --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}