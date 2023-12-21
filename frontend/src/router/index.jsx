import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import ProtectedRoute from "./ProtectedProvider";
import Home from "./pages/home";
import Auth from "./pages/auth";
import { AuthProvider } from "./pages/auth/AuthProvider";
import Users from "./pages/users";
import Library from "./pages/book";

export default function Router() {
  const router = createBrowserRouter([
    {
      path: '/auth',
      element: <Auth />
    },
    {
      path: "/",
      element: 
        <ProtectedRoute>
          <Home />
        </ProtectedRoute>
    },
    {
      path: "/users",
      element: 
        <ProtectedRoute>
          <Users />
        </ProtectedRoute>
    },
    {
      path: "/books",
      element: 
        <ProtectedRoute>
          <Library />
        </ProtectedRoute>
    },
  ]);

  return (
    <AuthProvider>
      <RouterProvider router={router} />
    </AuthProvider>
  )
}