pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh '''
                    # 1. Kill any existing instance running app.py
                    pkill -f "python3 app.py" || true

                    # 2. Tell Jenkins NOT to kill the background process after build ends
                    export JENKINS_NODE_COOKIE=dontKillMe
                    nohup python3 app.py > app.log 2>&1 &

                    # 3. Give it 2 seconds to bind port and print log
                    sleep 2
                    cat app.log
                '''
            }
        }
    }
}