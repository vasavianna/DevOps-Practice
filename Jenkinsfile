pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available!'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic validation...'
                sh 'python3 -m py_compile git_practice.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage completed!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
