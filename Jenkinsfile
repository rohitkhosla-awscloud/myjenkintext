pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh '''
                    # Stop any running instance on port 8000
                    fuser -k 8000/tcp || true

                    # Run Python app in background
                    nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}