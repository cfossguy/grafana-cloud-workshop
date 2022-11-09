import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
      { duration: '2m', target: 2 },
      { duration: '2m', target: 4 },
      { duration: '1m', target: 8 },
  ],
};

export default function () {
  http.get('http://localhost:8080/login');
  sleep(1);
  http.get('http://localhost:8080/account');
  sleep(2);
  http.get('http://localhost:8080/payment');
  sleep(3);
}
