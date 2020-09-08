# MANUALWORK

## DATA_UPLOAD

해당 테스트는 AWS에 설치되어있는 Maria DB의 접근권한이 필요합니다.

보안 관련 이슈가 있으므로 해당 절차서에는 기술하지 않습니다.

접속 정보가 필요할시 QA 팀으로 문의바랍니다.

### Test Case

#### 09_MANUALWORK_DATA_UPLOAD

- AWS MariaDB 접속

- 매뉴얼 테스트 데이터 삽입

  ```sql
  INSERT INTO
    `tb_support` (`SUPPORT_TYPE`, `TITLE`, `CATEGORY`, `IMAGE`, `DESCRIPTION`, `URL`, `CREATE_DATE`, `UPDATE_DATE`)
  VALUES
    ('manual','QA 매뉴얼 테스트','1',NULL,'QA 매뉴얼 테스트용 데이터입니다.','http://docs.192.168.102.136/manual/IRIS-Manual/IRIS-Common/index.html', now(), now());
  ```

- 튜토리얼 테스트 데이터 삽입

  ```sql
  INSERT INTO
    `tb_support` (`SUPPORT_TYPE`, `TITLE`, `CATEGORY`, `IMAGE`, `DESCRIPTION`, `URL`, `CREATE_DATE`, `UPDATE_DATE`)
  VALUES
    ('tutorial','QA 튜토리얼 테스트','1',NULL,'QA 튜토리얼 테스트용 데이터입니다.','http://docs.192.168.102.136/manual/IRIS-Manual/IRIS-Database/index.html', now(), now());
  ```

- 갤러리 테스트 데이터 삽입

  ```sql
  INSERT INTO
    `tb_support` (`SUPPORT_TYPE`, `TITLE`, `CATEGORY`, `IMAGE`, `DESCRIPTION`, `URL`, `CREATE_DATE`, `UPDATE_DATE`)
  VALUES
    ('gallery','QA 갤러리 테스트','1',NULL,'QA 갤러리 테스트용 데이터입니다.','http://docs.192.168.102.136/manual/IRIS-Manual/IRIS-Studio/index.html', now(), now());
  ```

- 매뉴얼 데이터가 제대로 삽입되었는지 확인

  ```sql
  select * from tb_support where support_type = 'manual';
  ```

- 갤러리 데이터가 제대로 삽입되었는지 확인

  ```sql
  select * from tb_support where support_type = 'gallery';
  ```

- 튜토리얼 데이터가 제대로 삽입되었는지 확인

  ```sql
  select * from tb_support where support_type = 'tutorial';
  ```
