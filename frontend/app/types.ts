declare global {

    interface IActivity {
        id: string,
        title: string,
        introduction: string,
        city: string,
        begin_time: string,
        end_time: string
    }

    interface IUserProfile {
        avatarId: string,
        nickname: string,
        sex: string,
        mbti: string,
        birthYear: Date
    }

    interface ITrip {
        userProfile: IUserProfile,
        activity: IActivity,
        date: Date,
        text: string,
        isPublic: boolean
    }

}