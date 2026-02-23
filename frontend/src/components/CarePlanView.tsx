import React from 'react';

interface Props {
    carePlan: string;
}

export const CarePlanView: React.FC<Props> = ({ carePlan }) => {
    return (
        <div>
            <div className="section">
                <h3>💊 Comprehensive Care Plan</h3>
                <div className="section-content">
                    <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.8' }}>
                        {carePlan}
                    </div>
                </div>
            </div>

            <div className="disclaimer">
                <strong>⚠️ IMPORTANT DISCLAIMER:</strong> This care plan is generated for
                educational and simulation purposes only. All treatment decisions must be made
                by a licensed healthcare provider.
            </div>
        </div>
    );
};