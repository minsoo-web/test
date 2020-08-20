// def MASTER_BUILD_NUMBER = Jenkins.instance.getItem('minsoo-test').lastSuccessfulBuild.number

pipeline {
    agent any
    
    options {
        ansiColor('xterm')
    }

    triggers {
        cron '''
        TZ=Asia/Seoul
        H 13 * * *
        '''
    }
    
    stages {
        stage('AUTO BUILD') {
            when {
                triggeredBy "TimerTrigger"
            }
            steps {
                echo "it is auto build ⏰"
                build(
                    job: 'minsoo-test',
                    wait: true,
                    parameters: [
                        string(name: 'build_target', value: 'IRIS-E2E-SAAS'),
                        string(name: 'menu_target', value: 'All'),
                        string(name: 'user', value: 'admin'),
                        string(name: 'container_number', value: "$BUILD_NUMBER")
                    ]
                )
            }
        }
        stage('DELETE CONTAINER') {
            steps {
                echo "✍️ CHECK CONTAINER EXIST"

                sh"""
                # 이전 빌드에 사용되었던 컨테이너를 삭제해준다.
                last_build_number=`expr $BUILD_NUMBER - 1`
                last_container_name=new-iris-e2e-$last_build_number

                if test ! -z "$(docker ps -af name=$last_container_name | grep -w $last_container_name$)"; then
                    echo "DELETE LAST BUILD CONTAINER"
                    docker rm -f $last_container_name
                fi
                """
                echo "END STAGE"
            }    
        }

        stage('PARAMS-E2E-TEST') {
            steps {
                echo "🔥 RUN PARAMETER E2E TEST"
                sh"""
                # 테스트 진행
                docker exec -t -w /root/IRIS-E2E-SAAS new-iris-e2e-${BUILD_NUMBER} qa-script/run-e2e-headless-side.sh
                """
                echo "END STAGE"
            }    
        }
    }
    
}