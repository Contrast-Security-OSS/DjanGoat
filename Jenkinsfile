node('docker') {
    stage('build') {
        checkout scm
        sh 'docker-compose run python'
        echo `which pylint`
    }
    stage ('lint') {
        docker.image('python').inside {
            stage('run linter') {
                echo `which pylint`
                sh "pylint app -f json > pylint_app.json"
                sh "pylint pygoat -f json > pylint_pygoat.json"
            }
        }
    }
    stage('test') {
        docker.image('python').inside {
            stage('run tests') {
                sh "python manage.py test app --settings=pygoat.docker_settings"
            }
        }
    }
    stage ('cleanup') {
         sh 'docker-compose down'
    }
}