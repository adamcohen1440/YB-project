// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase, set, ref, get} from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBeBudg1x-NOf-0Xg2zwo80kcAXNae2MaU",
  authDomain: "first-fun.firebaseapp.com",
  projectId: "first-fun",
  storageBucket: "first-fun.appspot.com",
  messagingSenderId: "12087997751",
  appId: "1:12087997751:web:579545a5555db9b323d6b2",
  measurementId: "G-3M4VL123C0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const writeBookData = (bookName, imageUrl, bookId) => {
  const db = getDatabase();
  const reference = ref(db, "books/" + bookId);

  set(reference, {
    name: bookName,
    image: imageUrl
  });
}

export const writeUserData = (userName, imageUrl, userId) => {
  const db = getDatabase();
  const reference = ref(db, "usernames/" + userId);

  set(reference, {
    name: userName,
    image: imageUrl
  })
}

export const getUserData = (username) => {
  const db = getDatabase();

  const data = get("usernames/" + username);
  
  return data;
}
