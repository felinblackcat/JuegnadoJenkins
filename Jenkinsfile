node {
    def commited_email = sh(script: "git rev-parse HEAD",  returnStdout: true).trim()
    def commited_hash = sh(script: "git log -1 --format='%ae'",  returnStdout: true).trim()
    def coverage
    echo commited_email
    echo commited_hash
    stage("BuildTesting") {
        def customImage = docker.build("juegnadojenkins:latest")
        customImage.inside{
            sh "ls"
        }
        coverage = sh(script: "docker run -w /var/jenkins_home/workspace/CI_CDtest_main --volumes-from 3a8d9b1a5e747074606855f78fa503260006fb9564d4e263bf39c8994a82b0a9 juegnadojenkins pytest --junitxml=testing.xml --cov=. --cov-fail-under=90 | grep TOTAL| awk '{print \$4}' | tr -d %", returnStdout: true).trim()
        sh "ls /var/jenkins_home/workspace/CI_CDtest_main/app"
    }
    echo "ls"
    junit 'testing.xml'
    echo coverage
    stage("CheckStaticCode") {
        echo "Hello, CheckStaticCode!"    
        sh 'docker run -e SONAR_HOST_URL="http://192.168.0.103:9000" -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=juegnadojenkins" -e SONAR_LOGIN="sqp_b688bf4f1611d6ce4029f0e7a9bb93ef8d1d2a7b" -w /var/jenkins_home/workspace/CI_CDtest_main --volumes-from 3a8d9b1a5e747074606855f78fa503260006fb9564d4e263bf39c8994a82b0a9 sonarsource/sonar-scanner-cli'
    }
    stage("RunUnitaryTest") {
        echo "Hello, RunUnitaryTest!"
     }
    stage("BuildPreprod") {
        echo "Hello, BuildPreprod!"
    }
    stage("IntegrationTest") {
        echo "Hello, IntegrationTest!"
    }
    stage("CheckCVE") {
        echo "Hello, CheckCVE!"
    }
    stage("SendRegistry") {
        echo "Hello, SendRegistry!"
    }
    stage("UATDeploy") {
        echo "Hello, UAT Deploy!"
    }
}