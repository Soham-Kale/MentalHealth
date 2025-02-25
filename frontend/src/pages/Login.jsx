// import React, { useState } from "react";
// import axios from "axios";
// import { useNavigate } from "react-router-dom";
// import { toast } from "react-toastify";
// import "react-toastify/dist/ReactToastify.css";

// const Login = () => {
//   const [isLogin, setIsLogin] = useState(true);
//   const [formData, setFormData] = useState({ 
//     username: "", 
//     email: "", 
//     password: "", 
//     confirmPassword: "" 
//   });
//   const navigate = useNavigate();

//   const handleChange = (e) => {
//     setFormData({ ...formData, [e.target.name]: e.target.value });
//   };



//   return (
//     <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-gray-100 to-gray-300">
//       <div className="w-96 p-6 bg-white shadow-lg rounded-lg">
//         {isLogin ? (
//           <>
//             <h2 className="text-2xl font-bold text-center">Welcome Back</h2>
//             <p className="text-sm text-gray-500 text-center mb-6">Enter your credentials to login</p>
//             <input
//               type="text"
//               name="username"
//               placeholder="Username"
//               value={formData.username}
//               onChange={handleChange}
//               className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500"
//             />
//             <input
//               type="password"
//               name="password"
//               placeholder="Password"
//               value={formData.password}
//               onChange={handleChange}
//               className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500"
//             />
//             <button 
//               onClick={handleSubmit} 
//               className="w-full bg-orange-500 text-white py-3 rounded-lg font-bold hover:bg-orange-600"
//             >
//               Login Now
//             </button>
//             <p className="text-center text-sm mt-4">
//               Don't have an account?{" "}
//               <span 
//                 className="text-orange-500 cursor-pointer" 
//                 onClick={() => setIsLogin(false)}
//               >
//                 Sign Up
//               </span>
//             </p>
//           </>
//         ) : (
//           <>
//             <h2 className="text-2xl font-bold text-center">Sign Up</h2>
//             <p className="text-sm text-gray-500 text-center mb-6">Create your account</p>
//             <input
//               type="text"
//               name="username"
//               placeholder="Username"
//               value={formData.username}
//               onChange={handleChange}
//               className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500"
//             />
//             <input
//               type="email"
//               name="email"
//               placeholder="Email"
//               value={formData.email}
//               onChange={handleChange}
//               className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500"
//             />
//             <input
//               type="password"
//               name="password"
//               placeholder="Password"
//               value={formData.password}
//               onChange={handleChange}
//               className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500"
//             />
//             <input
//               type="password"
//               name="confirmPassword"
//               placeholder="Confirm Password"
//               value={formData.confirmPassword}
//               onChange={handleChange}
//               className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500"
//             />
//             <button 
//               onClick={handleSubmit} 
//               className="w-full bg-orange-500 text-white py-3 rounded-lg font-bold hover:bg-orange-600"
//             >
//               Sign Up
//             </button>
//             <p className="text-center text-sm mt-4">
//               Already have an account?{" "}
//               <span 
//                 className="text-orange-500 cursor-pointer" 
//                 onClick={() => setIsLogin(true)}
//               >
//                 Login
//               </span>
//             </p>
//           </>
//         )}
//       </div>
//     </div>
//   );
// };

// export default Login;