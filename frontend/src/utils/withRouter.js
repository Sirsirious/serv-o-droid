import { useNavigate, useParams, useLocation } from 'react-router-dom';

export const withRouter = (Component) => {
  const Wrapper = (props) => {
    const navigate = useNavigate();
    const location = useLocation();
    const params = useParams();

    return (
      <Component
        {...props}
          router={{
            navigate,
            location,
            params,
          }}
        />
    );
  };
  
  return Wrapper;
};